package cucumberTest;

import org.junit.runner.RunWith; 
import cucumber.api.junit.*; 
import cucumber.runtime.junit.*;
import cucumber.api.CucumberOptions;
import stepDefinition.cucumberJavaLibrary;

@RunWith(Cucumber.class) 
@CucumberOptions(
		features = "feature"
		,glue={"stepDefinition"}
		, format = {"pretty", "html:target/Destination"} 
		)

public class Testrunner { }