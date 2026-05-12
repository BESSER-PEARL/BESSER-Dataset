





import java.util.List;
import java.util.ArrayList;

public class Jail  {

    private int JailPosition;
    private int jailFine;





    private Board1 board1;


    public Jail(
        int JailPosition,        int jailFine    ) {
        this.JailPosition = JailPosition;
        this.jailFine = jailFine;
    }


    public int getJailposition() {
        return JailPosition;
    }

    public void setJailposition(int JailPosition) {
        this.JailPosition = JailPosition;
    }
    public int getJailfine() {
        return jailFine;
    }

    public void setJailfine(int jailFine) {
        this.jailFine = jailFine;
    }

    public Board1 getBoard1() {
        return board1;
    }

    public void setBoard1(Board1 board1) {
        this.board1 = board1;
    }

}