





import java.util.List;
import java.util.ArrayList;

public class pltest_Circle  {

    private float area;
    private String diameter;
    private float circumference;





    private List<pltest_Red> pltest_reds;


    public pltest_Circle(
        float area,        String diameter,        float circumference    ) {
        this.area = area;
        this.diameter = diameter;
        this.circumference = circumference;
        this.pltest_reds = new ArrayList<>();
    }

    public pltest_Circle(
        float area,        String diameter,        float circumference        ArrayList<pltest_Red> pltest_reds    ) {
        this.area = area;
        this.diameter = diameter;
        this.circumference = circumference;
        this.pltest_reds = pltest_reds;
    }

    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }
    public String getDiameter() {
        return diameter;
    }

    public void setDiameter(String diameter) {
        this.diameter = diameter;
    }
    public float getCircumference() {
        return circumference;
    }

    public void setCircumference(float circumference) {
        this.circumference = circumference;
    }

    public List<pltest_Red> getPltest_reds() {
        return pltest_reds;
    }

    public void addPltest_red(Pltest_red pltest_red) {
        this.pltest_reds.add(pltest_red);
    }

}