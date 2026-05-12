





import java.util.List;
import java.util.ArrayList;

public class conference_makingOf_Participant  {

    private String attitude;
    private int age;



    public conference_makingOf_Participant(
        String attitude,        int age    ) {
        this.attitude = attitude;
        this.age = age;
    }


    public String getAttitude() {
        return attitude;
    }

    public void setAttitude(String attitude) {
        this.attitude = attitude;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}