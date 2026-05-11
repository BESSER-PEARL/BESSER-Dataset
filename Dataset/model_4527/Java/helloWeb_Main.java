





import java.util.List;
import java.util.ArrayList;

public class helloWeb_Main  {

    private String takeoff;
    private String land;





    private helloWeb_Program helloweb_program;


    public helloWeb_Main(
        String takeoff,        String land    ) {
        this.takeoff = takeoff;
        this.land = land;
    }


    public String getTakeoff() {
        return takeoff;
    }

    public void setTakeoff(String takeoff) {
        this.takeoff = takeoff;
    }
    public String getLand() {
        return land;
    }

    public void setLand(String land) {
        this.land = land;
    }

    public helloWeb_Program getHelloweb_program() {
        return helloweb_program;
    }

    public void setHelloweb_program(helloWeb_Program helloweb_program) {
        this.helloweb_program = helloweb_program;
    }

}