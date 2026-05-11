





import java.util.List;
import java.util.ArrayList;

public class vcml_ConfigurationProfileEntry  {

    private int sequence;





    private vcml_ConfigurationProfile vcml_configurationprofile;




    private vcml_Procedure vcml_procedure;




    private vcml_BOMItem vcml_bomitem;


    public vcml_ConfigurationProfileEntry(
        int sequence    ) {
        this.sequence = sequence;
    }


    public int getSequence() {
        return sequence;
    }

    public void setSequence(int sequence) {
        this.sequence = sequence;
    }

    public vcml_ConfigurationProfile getVcml_configurationprofile() {
        return vcml_configurationprofile;
    }

    public void setVcml_configurationprofile(vcml_ConfigurationProfile vcml_configurationprofile) {
        this.vcml_configurationprofile = vcml_configurationprofile;
    }
    public vcml_Procedure getVcml_procedure() {
        return vcml_procedure;
    }

    public void setVcml_procedure(vcml_Procedure vcml_procedure) {
        this.vcml_procedure = vcml_procedure;
    }
    public vcml_BOMItem getVcml_bomitem() {
        return vcml_bomitem;
    }

    public void setVcml_bomitem(vcml_BOMItem vcml_bomitem) {
        this.vcml_bomitem = vcml_bomitem;
    }

}