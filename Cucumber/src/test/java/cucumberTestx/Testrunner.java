package se.perekskog.cucumberTest;

import org.junit.runner.RunWith; 
import cucumber.api.junit.*; 
import cucumber.runtime.junit.*;
import cucumber.api.CucumberOptions;
import se.perekskog.stepDefinition.cucumberJavaLibrary;

@RunWith(Cucumber.class) 
@CucumberOptions(
		features = "cucumbertestfeature"
		,glue={"stepDefinitionx"}
		, format = {"pretty", "html:target/Destination"} 
		)

public class Testrunner { }