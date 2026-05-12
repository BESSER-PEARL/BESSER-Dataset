





import java.util.List;
import java.util.ArrayList;

public class checkers_CheckerMove  {

    private int illegalMove;
    private int incompleteMove;
    private int legalMove;



    public checkers_CheckerMove(
        int illegalMove,        int incompleteMove,        int legalMove    ) {
        this.illegalMove = illegalMove;
        this.incompleteMove = incompleteMove;
        this.legalMove = legalMove;
    }


    public int getIllegalmove() {
        return illegalMove;
    }

    public void setIllegalmove(int illegalMove) {
        this.illegalMove = illegalMove;
    }
    public int getIncompletemove() {
        return incompleteMove;
    }

    public void setIncompletemove(int incompleteMove) {
        this.incompleteMove = incompleteMove;
    }
    public int getLegalmove() {
        return legalMove;
    }

    public void setLegalmove(int legalMove) {
        this.legalMove = legalMove;
    }


}