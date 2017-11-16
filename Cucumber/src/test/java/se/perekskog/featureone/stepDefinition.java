package se.perekskog.featureone;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import se.perekskog.Calculator;
import cucumber.api.PendingException;

public class stepDefinition {

    private Calculator calculator;

    public stepDefinition(Calculator calculator)
    {
        this.calculator = calculator;
    }

@Given("^Load Readme$")
public void load_Readme() throws Throwable {
    System.out.println("===1===load_Readme");
    System.out.println("===1===state = " + calculator.state());
    // Write code here that turns the phrase above into concrete actions
    //throw new PendingException();
}

}