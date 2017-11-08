package cucumberTest;

import org.junit.runner.RunWith; 
import cucumber.api.junit.*; 
import cucumber.runtime.junit.*;
import cucumber.api.CucumberOptions;
import se.perekskog.featureone.stepDefinition;

@RunWith(Cucumber.class) 
@CucumberOptions(
		features = "cucumbertestfeature"
		,glue={"se.perekskog.common", "se.perekskog.featureone"}
		, format = {"pretty", "html:target/Destination"} 
		)

public class Testrunner { }