





import java.util.List;
import java.util.ArrayList;

public class mvc_Association extends Annotable {

    private int lowerBound;
    private String type;
    private boolean containment;
    private String name;
    private int upperBound;





    private mvc_Model mvc_model;


    public mvc_Association(
        int lowerBound,        String type,        boolean containment,        String name,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.type = type;
        this.containment = containment;
        this.name = name;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public mvc_Model getMvc_model() {
        return mvc_model;
    }

    public void setMvc_model(mvc_Model mvc_model) {
        this.mvc_model = mvc_model;
    }

}