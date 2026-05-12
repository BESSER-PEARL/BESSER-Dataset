





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int INITIAL_MONEY;
    private String name;
    private int position;
    private boolean isRetire;
    private None board;
    private int INITIAL_POSITION;
    private boolean isAI;
    private None rand;
    private String property;
    private boolean isBankrupt;
    private None money;
    private int PASS_GO_MONEY;



    public Player(
        int INITIAL_MONEY,        String name,        int position,        boolean isRetire,        None board,        int INITIAL_POSITION,        boolean isAI,        None rand,        String property,        boolean isBankrupt,        None money,        int PASS_GO_MONEY    ) {
        this.INITIAL_MONEY = INITIAL_MONEY;
        this.name = name;
        this.position = position;
        this.isRetire = isRetire;
        this.board = board;
        this.INITIAL_POSITION = INITIAL_POSITION;
        this.isAI = isAI;
        this.rand = rand;
        this.property = property;
        this.isBankrupt = isBankrupt;
        this.money = money;
        this.PASS_GO_MONEY = PASS_GO_MONEY;
    }


    public int getInitial_money() {
        return INITIAL_MONEY;
    }

    public void setInitial_money(int INITIAL_MONEY) {
        this.INITIAL_MONEY = INITIAL_MONEY;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public boolean getIsretire() {
        return isRetire;
    }

    public void setIsretire(boolean isRetire) {
        this.isRetire = isRetire;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public int getInitial_position() {
        return INITIAL_POSITION;
    }

    public void setInitial_position(int INITIAL_POSITION) {
        this.INITIAL_POSITION = INITIAL_POSITION;
    }
    public boolean getIsai() {
        return isAI;
    }

    public void setIsai(boolean isAI) {
        this.isAI = isAI;
    }
    public None getRand() {
        return rand;
    }

    public void setRand(None rand) {
        this.rand = rand;
    }
    public String getProperty() {
        return property;
    }

    public void setProperty(String property) {
        this.property = property;
    }
    public boolean getIsbankrupt() {
        return isBankrupt;
    }

    public void setIsbankrupt(boolean isBankrupt) {
        this.isBankrupt = isBankrupt;
    }
    public None getMoney() {
        return money;
    }

    public void setMoney(None money) {
        this.money = money;
    }
    public int getPass_go_money() {
        return PASS_GO_MONEY;
    }

    public void setPass_go_money(int PASS_GO_MONEY) {
        this.PASS_GO_MONEY = PASS_GO_MONEY;
    }


}