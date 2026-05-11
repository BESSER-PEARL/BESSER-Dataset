





import java.util.List;
import java.util.ArrayList;

public class express_CollectionType extends DataType {

    private int lowerBound;
    private boolean unique;
    private String name;
    private boolean many;
    private boolean opt;
    private int upperBound;



    public express_CollectionType(
        int lowerBound,        boolean unique,        String name,        boolean many,        boolean opt,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.unique = unique;
        this.name = name;
        this.many = many;
        this.opt = opt;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }
    public boolean getOpt() {
        return opt;
    }

    public void setOpt(boolean opt) {
        this.opt = opt;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }


}