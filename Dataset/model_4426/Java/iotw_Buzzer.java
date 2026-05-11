





import java.util.List;
import java.util.ArrayList;

public class iotw_Buzzer extends OutputDevice {

    private int Time;
    private int Tone;
    private String pin2;
    private String pin1;



    public iotw_Buzzer(
        int Time,        int Tone,        String pin2,        String pin1    ) {
        super(
        );
        this.Time = Time;
        this.Tone = Tone;
        this.pin2 = pin2;
        this.pin1 = pin1;
    }


    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }
    public int getTone() {
        return Tone;
    }

    public void setTone(int Tone) {
        this.Tone = Tone;
    }
    public String getPin2() {
        return pin2;
    }

    public void setPin2(String pin2) {
        this.pin2 = pin2;
    }
    public String getPin1() {
        return pin1;
    }

    public void setPin1(String pin1) {
        this.pin1 = pin1;
    }


}