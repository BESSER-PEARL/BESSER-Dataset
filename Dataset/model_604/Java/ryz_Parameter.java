





import java.util.List;
import java.util.ArrayList;

public class ryz_Parameter extends NamedElement {

    private boolean isList;
    private boolean isNullable;
    private String type;



    public ryz_Parameter(
        boolean isList,        boolean isNullable,        String type    ) {
        super(
        );
        this.isList = isList;
        this.isNullable = isNullable;
        this.type = type;
    }


    public boolean getIslist() {
        return isList;
    }

    public void setIslist(boolean isList) {
        this.isList = isList;
    }
    public boolean getIsnullable() {
        return isNullable;
    }

    public void setIsnullable(boolean isNullable) {
        this.isNullable = isNullable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}