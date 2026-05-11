





import java.util.List;
import java.util.ArrayList;

public class gyro_GyroSpecification  {

    private String name;





    private List<gyro_Sibling> gyro_siblings;




    private List<gyro_Child> gyro_childs;


    public gyro_GyroSpecification(
        String name    ) {
        this.name = name;
        this.gyro_siblings = new ArrayList<>();
        this.gyro_childs = new ArrayList<>();
    }

    public gyro_GyroSpecification(
        String name        ArrayList<gyro_Sibling> gyro_siblings,        ArrayList<gyro_Child> gyro_childs    ) {
        this.name = name;
        this.gyro_siblings = gyro_siblings;
        this.gyro_childs = gyro_childs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gyro_Sibling> getGyro_siblings() {
        return gyro_siblings;
    }

    public void addGyro_sibling(Gyro_sibling gyro_sibling) {
        this.gyro_siblings.add(gyro_sibling);
    }
    public List<gyro_Child> getGyro_childs() {
        return gyro_childs;
    }

    public void addGyro_child(Gyro_child gyro_child) {
        this.gyro_childs.add(gyro_child);
    }

}