





import java.util.List;
import java.util.ArrayList;

public class USE_Role  {

    private int upperBound;
    private boolean ordered;
    private String name;
    private int lowerBound;





    private USE_Association use_association;




    private USE_Class use_class;


    public USE_Role(
        int upperBound,        boolean ordered,        String name,        int lowerBound    ) {
        this.upperBound = upperBound;
        this.ordered = ordered;
        this.name = name;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public USE_Association getUse_association() {
        return use_association;
    }

    public void setUse_association(USE_Association use_association) {
        this.use_association = use_association;
    }
    public USE_Class getUse_class() {
        return use_class;
    }

    public void setUse_class(USE_Class use_class) {
        this.use_class = use_class;
    }

}