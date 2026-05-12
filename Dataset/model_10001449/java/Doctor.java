





import java.util.List;
import java.util.ArrayList;

public class Doctor  {

    private String timing;
    private String name;
    private boolean privateConsultancy;
    private String specilization;





    private Hospital hospital;


    public Doctor(
        String timing,        String name,        boolean privateConsultancy,        String specilization    ) {
        this.timing = timing;
        this.name = name;
        this.privateConsultancy = privateConsultancy;
        this.specilization = specilization;
    }


    public String getTiming() {
        return timing;
    }

    public void setTiming(String timing) {
        this.timing = timing;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getPrivateconsultancy() {
        return privateConsultancy;
    }

    public void setPrivateconsultancy(boolean privateConsultancy) {
        this.privateConsultancy = privateConsultancy;
    }
    public String getSpecilization() {
        return specilization;
    }

    public void setSpecilization(String specilization) {
        this.specilization = specilization;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}