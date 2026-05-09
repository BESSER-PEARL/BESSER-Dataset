





import java.util.List;
import java.util.ArrayList;

public class shr5_GegenstandStufen extends ModifikatorAttribute {

    private int antiTracing;
    private int protection;
    private int tracing;
    private int antiProtection;
    private int elektronik;
    private int computer;



    public shr5_GegenstandStufen(
        int antiTracing,        int protection,        int tracing,        int antiProtection,        int elektronik,        int computer    ) {
        super(
        );
        this.antiTracing = antiTracing;
        this.protection = protection;
        this.tracing = tracing;
        this.antiProtection = antiProtection;
        this.elektronik = elektronik;
        this.computer = computer;
    }


    public int getAntitracing() {
        return antiTracing;
    }

    public void setAntitracing(int antiTracing) {
        this.antiTracing = antiTracing;
    }
    public int getProtection() {
        return protection;
    }

    public void setProtection(int protection) {
        this.protection = protection;
    }
    public int getTracing() {
        return tracing;
    }

    public void setTracing(int tracing) {
        this.tracing = tracing;
    }
    public int getAntiprotection() {
        return antiProtection;
    }

    public void setAntiprotection(int antiProtection) {
        this.antiProtection = antiProtection;
    }
    public int getElektronik() {
        return elektronik;
    }

    public void setElektronik(int elektronik) {
        this.elektronik = elektronik;
    }
    public int getComputer() {
        return computer;
    }

    public void setComputer(int computer) {
        this.computer = computer;
    }


}