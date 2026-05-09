





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_TimerConfig extends Function {

    private String name;
    private int period;





    private MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage;


    public MicrocontrollerModeling_TimerConfig(
        String name,        int period    ) {
        super(
        );
        this.name = name;
        this.period = period;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPeriod() {
        return period;
    }

    public void setPeriod(int period) {
        this.period = period;
    }

    public MicrocontrollerModeling_CLanguage getMicrocontrollermodeling_clanguage() {
        return microcontrollermodeling_clanguage;
    }

    public void setMicrocontrollermodeling_clanguage(MicrocontrollerModeling_CLanguage microcontrollermodeling_clanguage) {
        this.microcontrollermodeling_clanguage = microcontrollermodeling_clanguage;
    }

}