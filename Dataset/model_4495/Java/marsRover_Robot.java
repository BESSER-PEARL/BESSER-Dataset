





import java.util.List;
import java.util.ArrayList;

public class marsRover_Robot  {

    private int special_speed;
    private String name;
    private String slave_address;
    private int drive_speed;



    public marsRover_Robot(
        int special_speed,        String name,        String slave_address,        int drive_speed    ) {
        this.special_speed = special_speed;
        this.name = name;
        this.slave_address = slave_address;
        this.drive_speed = drive_speed;
    }


    public int getSpecial_speed() {
        return special_speed;
    }

    public void setSpecial_speed(int special_speed) {
        this.special_speed = special_speed;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSlave_address() {
        return slave_address;
    }

    public void setSlave_address(String slave_address) {
        this.slave_address = slave_address;
    }
    public int getDrive_speed() {
        return drive_speed;
    }

    public void setDrive_speed(int drive_speed) {
        this.drive_speed = drive_speed;
    }


}