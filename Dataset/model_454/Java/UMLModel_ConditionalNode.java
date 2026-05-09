





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ConditionalNode extends StructuredActivityNode {

    private String isDeterminate;
    private String isAssured;



    public UMLModel_ConditionalNode(
        String isDeterminate,        String isAssured    ) {
        super(
        );
        this.isDeterminate = isDeterminate;
        this.isAssured = isAssured;
    }


    public String getIsdeterminate() {
        return isDeterminate;
    }

    public void setIsdeterminate(String isDeterminate) {
        this.isDeterminate = isDeterminate;
    }
    public String getIsassured() {
        return isAssured;
    }

    public void setIsassured(String isAssured) {
        this.isAssured = isAssured;
    }


}