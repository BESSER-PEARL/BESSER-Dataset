





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Semester  {

    private String Credits;
    private int Number;





    private tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program;


    public tDT4250_asssignment1_2_Semester(
        String Credits,        int Number    ) {
        this.Credits = Credits;
        this.Number = Number;
    }


    public String getCredits() {
        return Credits;
    }

    public void setCredits(String Credits) {
        this.Credits = Credits;
    }
    public int getNumber() {
        return Number;
    }

    public void setNumber(int Number) {
        this.Number = Number;
    }

    public tDT4250_asssignment1_2_Program getTdt4250_asssignment1_2_program() {
        return tdt4250_asssignment1_2_program;
    }

    public void setTdt4250_asssignment1_2_program(tDT4250_asssignment1_2_Program tdt4250_asssignment1_2_program) {
        this.tdt4250_asssignment1_2_program = tdt4250_asssignment1_2_program;
    }

}