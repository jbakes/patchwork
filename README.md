# Patchwork

## API

### Running Patchwork

```python
import Game as game

env = game.make()
env.reset()

# ... play game    
```

### API Methods

The API exposes the following methods:

 - step() returns observation, reward, done, info
 
env has the following attributes:
 
 - action_space
 - observation_space (might be nice to implement as a Box with high/low attributes)
 
