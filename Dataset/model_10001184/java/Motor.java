





import java.util.List;
import java.util.ArrayList;

public class Motor  {

    private String Durable;
    private String Suitable_Speed;



    public Motor(
        String Durable,        String Suitable_Speed    ) {
        this.Durable = Durable;
        this.Suitable_Speed = Suitable_Speed;
    }


    public String getDurable() {
        return Durable;
    }

    public void setDurable(String Durable) {
        this.Durable = Durable;
    }
    public String getSuitable_speed() {
        return Suitable_Speed;
    }

    public void setSuitable_speed(String Suitable_Speed) {
        this.Suitable_Speed = Suitable_Speed;
    }


}