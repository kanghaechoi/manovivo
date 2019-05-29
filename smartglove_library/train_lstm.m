function [net] = train_lstm(features, labels)
%% Long short-term memory network training sequence

x = features;
y = labels;
%y_vector = ind2vec(y);
%x_cell = mat2cell(x, 1);
y_categories = categorical(y);


% Sort the data by length
numObservations = numel(x);

for i=1:numObservations
    sequence = x{i,1};
    [m, n] = size(sequence);
    sequenceLengths(i) = m;
end

[sequenceLengths,idx] = sort(sequenceLengths);
x = x(idx);
y_categories = y_categories(idx);



input_size = 11;
hidden_layer_size = 100;
output_size = 2;

layers = [sequenceInputLayer(input_size), lstmLayer(hidden_layer_size, 'OutputMode', 'last'), ...
    fullyConnectedLayer(output_size), softmaxLayer, classificationLayer];

max_epochs = 100;
mini_batch_size = 100;

options = trainingOptions('adam', 'ExecutionEnvironment', 'auto', ...,
    'MaxEpochs', max_epochs, 'MiniBatchSize', mini_batch_size, ...
    'GradientThreshold', 1, 'Verbose', false, 'Plots', 'training-progress');




net = trainNetwork(x, y_categories, layers, options);

end

