





import java.util.List;
import java.util.ArrayList;

public class USE_Role  {

    private boolean ordered;
    private int upperBound;
    private int lowerBound;
    private String name;





    private USE_Class use_class;




    private USE_Association use_association;


    public USE_Role(
        boolean ordered,        int upperBound,        int lowerBound,        String name    ) {
        this.ordered = ordered;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.name = name;
    }


    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Class getUse_class() {
        return use_class;
    }

    public void setUse_class(USE_Class use_class) {
        this.use_class = use_class;
    }
    public USE_Association getUse_association() {
        return use_association;
    }

    public void setUse_association(USE_Association use_association) {
        this.use_association = use_association;
    }

}