import React from 'react';
import { Jumbotron, Button } from 'react-bootstrap';

const Welcome = () => (
  <Jumbotron>
    <h1>Easy Photos</h1>
    <p>
      This is simple application that retrieves photos using Unsplash API. In
      order to start enter any search term in the input field.
    </p>
    <Button href="https://www.unsplash.com" target="_blank">
      Go to Unsplash
    </Button>
  </Jumbotron>
);

export default Welcome;
