





import java.util.List;
import java.util.ArrayList;

public class turtlebotmission_Area  {

    private int xmax;
    private int ymax;





    private turtlebotmission_TurtleBot turtlebotmission_turtlebot;


    public turtlebotmission_Area(
        int xmax,        int ymax    ) {
        this.xmax = xmax;
        this.ymax = ymax;
    }


    public int getXmax() {
        return xmax;
    }

    public void setXmax(int xmax) {
        this.xmax = xmax;
    }
    public int getYmax() {
        return ymax;
    }

    public void setYmax(int ymax) {
        this.ymax = ymax;
    }

    public turtlebotmission_TurtleBot getTurtlebotmission_turtlebot() {
        return turtlebotmission_turtlebot;
    }

    public void setTurtlebotmission_turtlebot(turtlebotmission_TurtleBot turtlebotmission_turtlebot) {
        this.turtlebotmission_turtlebot = turtlebotmission_turtlebot;
    }

}