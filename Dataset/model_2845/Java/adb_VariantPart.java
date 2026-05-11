





import java.util.List;
import java.util.ArrayList;

public class adb_VariantPart  {

    private String name;





    private adb_OptVariantPart adb_optvariantpart;


    public adb_VariantPart(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_OptVariantPart getAdb_optvariantpart() {
        return adb_optvariantpart;
    }

    public void setAdb_optvariantpart(adb_OptVariantPart adb_optvariantpart) {
        this.adb_optvariantpart = adb_optvariantpart;
    }

}