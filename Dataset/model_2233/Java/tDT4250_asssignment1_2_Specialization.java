





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Specialization  {

    private String Name;





    private List<tDT4250_asssignment1_2_Semester> tdt4250_asssignment1_2_semesters;




    private tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program;




    private List<tDT4250_asssignment1_2_Specialization> tdt4250_asssignment1_2_specializations;


    public tDT4250_asssignment1_2_Specialization(
        String Name    ) {
        this.Name = Name;
        this.tdt4250_asssignment1_2_semesters = new ArrayList<>();
        this.tdt4250_asssignment1_2_specializations = new ArrayList<>();
    }

    public tDT4250_asssignment1_2_Specialization(
        String Name        ArrayList<tDT4250_asssignment1_2_Semester> tdt4250_asssignment1_2_semesters,        ArrayList<tDT4250_asssignment1_2_Specialization> tdt4250_asssignment1_2_specializations    ) {
        this.Name = Name;
        this.tdt4250_asssignment1_2_semesters = tdt4250_asssignment1_2_semesters;
        this.tdt4250_asssignment1_2_specializations = tdt4250_asssignment1_2_specializations;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<tDT4250_asssignment1_2_Semester> getTdt4250_asssignment1_2_semesters() {
        return tdt4250_asssignment1_2_semesters;
    }

    public void addTdt4250_asssignment1_2_semester(Tdt4250_asssignment1_2_semester tdt4250_asssignment1_2_semester) {
        this.tdt4250_asssignment1_2_semesters.add(tdt4250_asssignment1_2_semester);
    }
    public tDT4250_asssignment1_2_Program getTdt4250_asssignment1_2_program() {
        return tdt4250_asssignment1_2_program;
    }

    public void setTdt4250_asssignment1_2_program(tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program) {
        this.tdt4250_asssignment1_2_program = tdt4250_asssignment1_2_program;
    }
    public List<tDT4250_asssignment1_2_Specialization> getTdt4250_asssignment1_2_specializations() {
        return tdt4250_asssignment1_2_specializations;
    }

    public void addTdt4250_asssignment1_2_specialization(Tdt4250_asssignment1_2_specialization tdt4250_asssignment1_2_specialization) {
        this.tdt4250_asssignment1_2_specializations.add(tdt4250_asssignment1_2_specialization);
    }

}