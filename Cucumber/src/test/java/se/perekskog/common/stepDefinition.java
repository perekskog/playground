package se.perekskog.common;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.PendingException;
import se.perekskog.Calculator;

public class stepDefinition {

    private Calculator calculator;

@Given("^Connect to Test server$")
public void connect_to_Test_server() throws Throwable {
    System.out.println("===C===connect_to_Test_server");

    calculator = new Calculator();
    calculator.add(5);
    // Write code here that turns the phrase above into concrete actions
    //throw new PendingException();
}

@Then("^cleanup locally created files$")
public void cleanup_locally_created_files() throws Throwable {
    System.out.println("===C===cleanup_locally_created_files");
    calculator.add(3);
    System.out.println("===C===" + calculator.state());
    // Write code here that turns the phrase above into concrete actions
    //throw new PendingException();
}

}