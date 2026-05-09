





import java.util.List;
import java.util.ArrayList;

public class shadowrun_GegenstandStufen  {

    private int Elektronik;
    private int Computer;
    private int AntiProtection;
    private int Tracing;
    private int Protection;
    private int AntiTracing;



    public shadowrun_GegenstandStufen(
        int Elektronik,        int Computer,        int AntiProtection,        int Tracing,        int Protection,        int AntiTracing    ) {
        this.Elektronik = Elektronik;
        this.Computer = Computer;
        this.AntiProtection = AntiProtection;
        this.Tracing = Tracing;
        this.Protection = Protection;
        this.AntiTracing = AntiTracing;
    }


    public int getElektronik() {
        return Elektronik;
    }

    public void setElektronik(int Elektronik) {
        this.Elektronik = Elektronik;
    }
    public int getComputer() {
        return Computer;
    }

    public void setComputer(int Computer) {
        this.Computer = Computer;
    }
    public int getAntiprotection() {
        return AntiProtection;
    }

    public void setAntiprotection(int AntiProtection) {
        this.AntiProtection = AntiProtection;
    }
    public int getTracing() {
        return Tracing;
    }

    public void setTracing(int Tracing) {
        this.Tracing = Tracing;
    }
    public int getProtection() {
        return Protection;
    }

    public void setProtection(int Protection) {
        this.Protection = Protection;
    }
    public int getAntitracing() {
        return AntiTracing;
    }

    public void setAntitracing(int AntiTracing) {
        this.AntiTracing = AntiTracing;
    }


}