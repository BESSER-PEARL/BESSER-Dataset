





import java.util.List;
import java.util.ArrayList;

public class gyro_LED extends Actuate {

    private String status;



    public gyro_LED(
        String status    ) {
        super(
        );
        this.status = status;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


}