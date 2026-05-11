





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_Player extends HockeyleagueObject {

    private String birthplace;
    private String birthdate;
    private int heightValue;
    private String shot;
    private String weightMesurement;
    private int weightValue;
    private int number;
    private String heightMesurement;



    public hockeyleague_Player(
        String birthplace,        String birthdate,        int heightValue,        String shot,        String weightMesurement,        int weightValue,        int number,        String heightMesurement    ) {
        super(
        );
        this.birthplace = birthplace;
        this.birthdate = birthdate;
        this.heightValue = heightValue;
        this.shot = shot;
        this.weightMesurement = weightMesurement;
        this.weightValue = weightValue;
        this.number = number;
        this.heightMesurement = heightMesurement;
    }


    public String getBirthplace() {
        return birthplace;
    }

    public void setBirthplace(String birthplace) {
        this.birthplace = birthplace;
    }
    public String getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(String birthdate) {
        this.birthdate = birthdate;
    }
    public int getHeightvalue() {
        return heightValue;
    }

    public void setHeightvalue(int heightValue) {
        this.heightValue = heightValue;
    }
    public String getShot() {
        return shot;
    }

    public void setShot(String shot) {
        this.shot = shot;
    }
    public String getWeightmesurement() {
        return weightMesurement;
    }

    public void setWeightmesurement(String weightMesurement) {
        this.weightMesurement = weightMesurement;
    }
    public int getWeightvalue() {
        return weightValue;
    }

    public void setWeightvalue(int weightValue) {
        this.weightValue = weightValue;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getHeightmesurement() {
        return heightMesurement;
    }

    public void setHeightmesurement(String heightMesurement) {
        this.heightMesurement = heightMesurement;
    }


}