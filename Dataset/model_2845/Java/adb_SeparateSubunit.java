





import java.util.List;
import java.util.ArrayList;

public class adb_SeparateSubunit extends Unit {

    private String parentUnitName;



    public adb_SeparateSubunit(
        String parentUnitName    ) {
        super(
        );
        this.parentUnitName = parentUnitName;
    }


    public String getParentunitname() {
        return parentUnitName;
    }

    public void setParentunitname(String parentUnitName) {
        this.parentUnitName = parentUnitName;
    }


}