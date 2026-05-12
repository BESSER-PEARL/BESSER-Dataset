





import java.util.List;
import java.util.ArrayList;

public class Jail  {

    private int jailFine;
    private int JailPosition;





    private Board1 board1;


    public Jail(
        int jailFine,        int JailPosition    ) {
        this.jailFine = jailFine;
        this.JailPosition = JailPosition;
    }


    public int getJailfine() {
        return jailFine;
    }

    public void setJailfine(int jailFine) {
        this.jailFine = jailFine;
    }
    public int getJailposition() {
        return JailPosition;
    }

    public void setJailposition(int JailPosition) {
        this.JailPosition = JailPosition;
    }

    public Board1 getBoard1() {
        return board1;
    }

    public void setBoard1(Board1 board1) {
        this.board1 = board1;
    }

}