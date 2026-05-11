





import java.util.List;
import java.util.ArrayList;

public class iotw_Buzzer extends OutputDevice {

    private int Tone;
    private String pin1;
    private String pin2;
    private int Time;



    public iotw_Buzzer(
        int Tone,        String pin1,        String pin2,        int Time    ) {
        super(
        );
        this.Tone = Tone;
        this.pin1 = pin1;
        this.pin2 = pin2;
        this.Time = Time;
    }


    public int getTone() {
        return Tone;
    }

    public void setTone(int Tone) {
        this.Tone = Tone;
    }
    public String getPin1() {
        return pin1;
    }

    public void setPin1(String pin1) {
        this.pin1 = pin1;
    }
    public String getPin2() {
        return pin2;
    }

    public void setPin2(String pin2) {
        this.pin2 = pin2;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }


}