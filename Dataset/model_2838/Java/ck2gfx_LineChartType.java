





import java.util.List;
import java.util.ArrayList;

public class ck2gfx_LineChartType  {

    private String name;
    private int lineWidth;





    private ck2gfx_Coordinates ck2gfx_coordinates;


    public ck2gfx_LineChartType(
        String name,        int lineWidth    ) {
        this.name = name;
        this.lineWidth = lineWidth;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }

    public ck2gfx_Coordinates getCk2gfx_coordinates() {
        return ck2gfx_coordinates;
    }

    public void setCk2gfx_coordinates(ck2gfx_Coordinates ck2gfx_coordinates) {
        this.ck2gfx_coordinates = ck2gfx_coordinates;
    }

}