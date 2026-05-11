





import java.util.List;
import java.util.ArrayList;

public class testmodel_Association extends ModelElement {

    private String secondLabel;
    private String firstLabel;





    private testmodel_Class testmodel_class;




    private testmodel_Class testmodel_class;


    public testmodel_Association(
        String secondLabel,        String firstLabel    ) {
        super(
        );
        this.secondLabel = secondLabel;
        this.firstLabel = firstLabel;
    }


    public String getSecondlabel() {
        return secondLabel;
    }

    public void setSecondlabel(String secondLabel) {
        this.secondLabel = secondLabel;
    }
    public String getFirstlabel() {
        return firstLabel;
    }

    public void setFirstlabel(String firstLabel) {
        this.firstLabel = firstLabel;
    }

    public testmodel_Class getTestmodel_class() {
        return testmodel_class;
    }

    public void setTestmodel_class(testmodel_Class testmodel_class) {
        this.testmodel_class = testmodel_class;
    }
    public testmodel_Class getTestmodel_class() {
        return testmodel_class;
    }

    public void setTestmodel_class(testmodel_Class testmodel_class) {
        this.testmodel_class = testmodel_class;
    }

}