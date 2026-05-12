





import java.util.List;
import java.util.ArrayList;

public class Dice  {

    private int secondValue;
    private int firstValue;
    private None randomNumber;





    private Board1 board1;


    public Dice(
        int secondValue,        int firstValue,        None randomNumber    ) {
        this.secondValue = secondValue;
        this.firstValue = firstValue;
        this.randomNumber = randomNumber;
    }


    public int getSecondvalue() {
        return secondValue;
    }

    public void setSecondvalue(int secondValue) {
        this.secondValue = secondValue;
    }
    public int getFirstvalue() {
        return firstValue;
    }

    public void setFirstvalue(int firstValue) {
        this.firstValue = firstValue;
    }
    public None getRandomnumber() {
        return randomNumber;
    }

    public void setRandomnumber(None randomNumber) {
        this.randomNumber = randomNumber;
    }

    public Board1 getBoard1() {
        return board1;
    }

    public void setBoard1(Board1 board1) {
        this.board1 = board1;
    }

}