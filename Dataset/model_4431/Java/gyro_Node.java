





import java.util.List;
import java.util.ArrayList;

public class gyro_Node  {

    private String name;





    private gyro_Sibling gyro_sibling;




    private gyro_Child gyro_child;




    private gyro_GyroSpecification gyro_gyrospecification;




    private gyro_Sibling gyro_sibling;


    public gyro_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gyro_Sibling getGyro_sibling() {
        return gyro_sibling;
    }

    public void setGyro_sibling(gyro_Sibling gyro_sibling) {
        this.gyro_sibling = gyro_sibling;
    }
    public gyro_Child getGyro_child() {
        return gyro_child;
    }

    public void setGyro_child(gyro_Child gyro_child) {
        this.gyro_child = gyro_child;
    }
    public gyro_GyroSpecification getGyro_gyrospecification() {
        return gyro_gyrospecification;
    }

    public void setGyro_gyrospecification(gyro_GyroSpecification gyro_gyrospecification) {
        this.gyro_gyrospecification = gyro_gyrospecification;
    }
    public gyro_Sibling getGyro_sibling() {
        return gyro_sibling;
    }

    public void setGyro_sibling(gyro_Sibling gyro_sibling) {
        this.gyro_sibling = gyro_sibling;
    }

}