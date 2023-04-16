import React from 'react';
import { Navbar } from 'react-bootstrap';
import { Container } from 'react-bootstrap';

const Header = ( { title } ) => {
    return (
    <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="/ ">{title}</Navbar.Brand>
        </Container>
      </Navbar>
    )
};

export default Header;