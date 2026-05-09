





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Deviceset  {

    private boolean uservalue;
    private String prefix;
    private String name;





    private eaglemodel_Devicesets eaglemodel_devicesets;


    public eaglemodel_Deviceset(
        boolean uservalue,        String prefix,        String name    ) {
        this.uservalue = uservalue;
        this.prefix = prefix;
        this.name = name;
    }


    public boolean getUservalue() {
        return uservalue;
    }

    public void setUservalue(boolean uservalue) {
        this.uservalue = uservalue;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eaglemodel_Devicesets getEaglemodel_devicesets() {
        return eaglemodel_devicesets;
    }

    public void setEaglemodel_devicesets(eaglemodel_Devicesets eaglemodel_devicesets) {
        this.eaglemodel_devicesets = eaglemodel_devicesets;
    }

}