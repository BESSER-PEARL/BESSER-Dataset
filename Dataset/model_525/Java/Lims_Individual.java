





import java.util.List;
import java.util.ArrayList;

public class Lims_Individual  {

    private String gender;
    private String name;





    private Lims_Individual lims_individual;




    private List<Lims_Sample> lims_samples;




    private Lims_Family lims_family;




    private Lims_Sample lims_sample;




    private Lims_Individual lims_individual;




    private Lims_Family lims_family;


    public Lims_Individual(
        String gender,        String name    ) {
        this.gender = gender;
        this.name = name;
        this.lims_samples = new ArrayList<>();
    }

    public Lims_Individual(
        String gender,        String name        ArrayList<Lims_Sample> lims_samples    ) {
        this.gender = gender;
        this.name = name;
        this.lims_samples = lims_samples;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Lims_Individual getLims_individual() {
        return lims_individual;
    }

    public void setLims_individual(Lims_Individual lims_individual) {
        this.lims_individual = lims_individual;
    }
    public List<Lims_Sample> getLims_samples() {
        return lims_samples;
    }

    public void addLims_sample(Lims_sample lims_sample) {
        this.lims_samples.add(lims_sample);
    }
    public Lims_Family getLims_family() {
        return lims_family;
    }

    public void setLims_family(Lims_Family lims_family) {
        this.lims_family = lims_family;
    }
    public Lims_Sample getLims_sample() {
        return lims_sample;
    }

    public void setLims_sample(Lims_Sample lims_sample) {
        this.lims_sample = lims_sample;
    }
    public Lims_Individual getLims_individual() {
        return lims_individual;
    }

    public void setLims_individual(Lims_Individual lims_individual) {
        this.lims_individual = lims_individual;
    }
    public Lims_Family getLims_family() {
        return lims_family;
    }

    public void setLims_family(Lims_Family lims_family) {
        this.lims_family = lims_family;
    }

}