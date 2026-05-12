





import java.util.List;
import java.util.ArrayList;

public class FingerprintReader  {

    private float Y__Cord;
    private int miniType;
    private None MiniType;
    private int Emp_Id;
    private float X_cord;
    private float Angle;





    private Attendance attendance;


    public FingerprintReader(
        float Y__Cord,        int miniType,        None MiniType,        int Emp_Id,        float X_cord,        float Angle    ) {
        this.Y__Cord = Y__Cord;
        this.miniType = miniType;
        this.MiniType = MiniType;
        this.Emp_Id = Emp_Id;
        this.X_cord = X_cord;
        this.Angle = Angle;
    }


    public float getY__cord() {
        return Y__Cord;
    }

    public void setY__cord(float Y__Cord) {
        this.Y__Cord = Y__Cord;
    }
    public int getMinitype() {
        return miniType;
    }

    public void setMinitype(int miniType) {
        this.miniType = miniType;
    }
    public None getMinitype() {
        return MiniType;
    }

    public void setMinitype(None MiniType) {
        this.MiniType = MiniType;
    }
    public int getEmp_id() {
        return Emp_Id;
    }

    public void setEmp_id(int Emp_Id) {
        this.Emp_Id = Emp_Id;
    }
    public float getX_cord() {
        return X_cord;
    }

    public void setX_cord(float X_cord) {
        this.X_cord = X_cord;
    }
    public float getAngle() {
        return Angle;
    }

    public void setAngle(float Angle) {
        this.Angle = Angle;
    }

    public Attendance getAttendance() {
        return attendance;
    }

    public void setAttendance(Attendance attendance) {
        this.attendance = attendance;
    }

}