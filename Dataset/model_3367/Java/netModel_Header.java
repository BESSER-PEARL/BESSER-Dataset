





import java.util.List;
import java.util.ArrayList;

public class netModel_Header  {

    private String value;
    private String name;





    private netModel_HeaderBlock netmodel_headerblock;


    public netModel_Header(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public netModel_HeaderBlock getNetmodel_headerblock() {
        return netmodel_headerblock;
    }

    public void setNetmodel_headerblock(netModel_HeaderBlock netmodel_headerblock) {
        this.netmodel_headerblock = netmodel_headerblock;
    }

}