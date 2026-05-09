





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ExpansionRegion extends StructuredActivityNode {

    private String inputElement;
    private String outputElement;
    private String mode;



    public UMLModel_ExpansionRegion(
        String inputElement,        String outputElement,        String mode    ) {
        super(
        );
        this.inputElement = inputElement;
        this.outputElement = outputElement;
        this.mode = mode;
    }


    public String getInputelement() {
        return inputElement;
    }

    public void setInputelement(String inputElement) {
        this.inputElement = inputElement;
    }
    public String getOutputelement() {
        return outputElement;
    }

    public void setOutputelement(String outputElement) {
        this.outputElement = outputElement;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}