





import java.util.List;
import java.util.ArrayList;

public class pimm_Expression extends PiMMVisitable {

    private String string;





    private pimm_Parameter pimm_parameter;


    public pimm_Expression(
        String string    ) {
        super(
        );
        this.string = string;
    }


    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public pimm_Parameter getPimm_parameter() {
        return pimm_parameter;
    }

    public void setPimm_parameter(pimm_Parameter pimm_parameter) {
        this.pimm_parameter = pimm_parameter;
    }

}