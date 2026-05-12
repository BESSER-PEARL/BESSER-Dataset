





import java.util.List;
import java.util.ArrayList;

public class Controlling_Circuit  {

    private String MIcro_processor;
    private String Software;



    public Controlling_Circuit(
        String MIcro_processor,        String Software    ) {
        this.MIcro_processor = MIcro_processor;
        this.Software = Software;
    }


    public String getMicro_processor() {
        return MIcro_processor;
    }

    public void setMicro_processor(String MIcro_processor) {
        this.MIcro_processor = MIcro_processor;
    }
    public String getSoftware() {
        return Software;
    }

    public void setSoftware(String Software) {
        this.Software = Software;
    }


}