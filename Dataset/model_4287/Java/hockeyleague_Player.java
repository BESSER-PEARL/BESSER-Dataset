





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_Player extends HockeyleagueObject {

    private String heightMesurement;
    private int heightValue;
    private int weightValue;
    private String shot;
    private int number;
    private String weightMesurement;
    private String birthplace;
    private String birthdate;



    public hockeyleague_Player(
        String heightMesurement,        int heightValue,        int weightValue,        String shot,        int number,        String weightMesurement,        String birthplace,        String birthdate    ) {
        super(
        );
        this.heightMesurement = heightMesurement;
        this.heightValue = heightValue;
        this.weightValue = weightValue;
        this.shot = shot;
        this.number = number;
        this.weightMesurement = weightMesurement;
        this.birthplace = birthplace;
        this.birthdate = birthdate;
    }


    public String getHeightmesurement() {
        return heightMesurement;
    }

    public void setHeightmesurement(String heightMesurement) {
        this.heightMesurement = heightMesurement;
    }
    public int getHeightvalue() {
        return heightValue;
    }

    public void setHeightvalue(int heightValue) {
        this.heightValue = heightValue;
    }
    public int getWeightvalue() {
        return weightValue;
    }

    public void setWeightvalue(int weightValue) {
        this.weightValue = weightValue;
    }
    public String getShot() {
        return shot;
    }

    public void setShot(String shot) {
        this.shot = shot;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getWeightmesurement() {
        return weightMesurement;
    }

    public void setWeightmesurement(String weightMesurement) {
        this.weightMesurement = weightMesurement;
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


}