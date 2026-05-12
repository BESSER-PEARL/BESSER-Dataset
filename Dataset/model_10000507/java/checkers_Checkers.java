





import java.util.List;
import java.util.ArrayList;

public class checkers_Checkers  {

    private int endY;
    private None diff;
    private int yellowKing;
    private None c2;
    private int preToMove1;
    private int empty;
    private None yellowK;
    private None snp;
    private boolean highlight;
    private None snB;
    private int yellowNormal;
    private None redN;
    private int won;
    private String preBoard1;
    private None yellowN;
    private int preToMove2;
    private None hlp;
    private None bp;
    private None players;
    private None rp;
    private None col;
    private None mup;
    private String preBoard3;
    private None msg;
    private None colors;
    private None bpt;
    private int preToMove3;
    private None mode;
    private None p1;
    private int difficulty;
    private None rkt;
    private None level;
    private String selectedColor;
    private int undoCount;
    private int redKing;
    private None hlpB;
    private None nwB;
    private boolean movable;
    private None g;
    private boolean silent;
    private None rk;
    private None p2;
    private None bk;
    private boolean incomplete;
    private int currType;
    private None winPoint;
    private int loser;
    private None rpt;
    private None unB;
    private int toMove;
    private int selectedMode;
    private String board;
    private String preBoard2;
    private None c1;
    private None redK;
    private None bkt;
    private int redNormal;



    public checkers_Checkers(
        int endY,        None diff,        int yellowKing,        None c2,        int preToMove1,        int empty,        None yellowK,        None snp,        boolean highlight,        None snB,        int yellowNormal,        None redN,        int won,        String preBoard1,        None yellowN,        int preToMove2,        None hlp,        None bp,        None players,        None rp,        None col,        None mup,        String preBoard3,        None msg,        None colors,        None bpt,        int preToMove3,        None mode,        None p1,        int difficulty,        None rkt,        None level,        String selectedColor,        int undoCount,        int redKing,        None hlpB,        None nwB,        boolean movable,        None g,        boolean silent,        None rk,        None p2,        None bk,        boolean incomplete,        int currType,        None winPoint,        int loser,        None rpt,        None unB,        int toMove,        int selectedMode,        String board,        String preBoard2,        None c1,        None redK,        None bkt,        int redNormal    ) {
        this.endY = endY;
        this.diff = diff;
        this.yellowKing = yellowKing;
        this.c2 = c2;
        this.preToMove1 = preToMove1;
        this.empty = empty;
        this.yellowK = yellowK;
        this.snp = snp;
        this.highlight = highlight;
        this.snB = snB;
        this.yellowNormal = yellowNormal;
        this.redN = redN;
        this.won = won;
        this.preBoard1 = preBoard1;
        this.yellowN = yellowN;
        this.preToMove2 = preToMove2;
        this.hlp = hlp;
        this.bp = bp;
        this.players = players;
        this.rp = rp;
        this.col = col;
        this.mup = mup;
        this.preBoard3 = preBoard3;
        this.msg = msg;
        this.colors = colors;
        this.bpt = bpt;
        this.preToMove3 = preToMove3;
        this.mode = mode;
        this.p1 = p1;
        this.difficulty = difficulty;
        this.rkt = rkt;
        this.level = level;
        this.selectedColor = selectedColor;
        this.undoCount = undoCount;
        this.redKing = redKing;
        this.hlpB = hlpB;
        this.nwB = nwB;
        this.movable = movable;
        this.g = g;
        this.silent = silent;
        this.rk = rk;
        this.p2 = p2;
        this.bk = bk;
        this.incomplete = incomplete;
        this.currType = currType;
        this.winPoint = winPoint;
        this.loser = loser;
        this.rpt = rpt;
        this.unB = unB;
        this.toMove = toMove;
        this.selectedMode = selectedMode;
        this.board = board;
        this.preBoard2 = preBoard2;
        this.c1 = c1;
        this.redK = redK;
        this.bkt = bkt;
        this.redNormal = redNormal;
    }


    public int getEndy() {
        return endY;
    }

    public void setEndy(int endY) {
        this.endY = endY;
    }
    public None getDiff() {
        return diff;
    }

    public void setDiff(None diff) {
        this.diff = diff;
    }
    public int getYellowking() {
        return yellowKing;
    }

    public void setYellowking(int yellowKing) {
        this.yellowKing = yellowKing;
    }
    public None getC2() {
        return c2;
    }

    public void setC2(None c2) {
        this.c2 = c2;
    }
    public int getPretomove1() {
        return preToMove1;
    }

    public void setPretomove1(int preToMove1) {
        this.preToMove1 = preToMove1;
    }
    public int getEmpty() {
        return empty;
    }

    public void setEmpty(int empty) {
        this.empty = empty;
    }
    public None getYellowk() {
        return yellowK;
    }

    public void setYellowk(None yellowK) {
        this.yellowK = yellowK;
    }
    public None getSnp() {
        return snp;
    }

    public void setSnp(None snp) {
        this.snp = snp;
    }
    public boolean getHighlight() {
        return highlight;
    }

    public void setHighlight(boolean highlight) {
        this.highlight = highlight;
    }
    public None getSnb() {
        return snB;
    }

    public void setSnb(None snB) {
        this.snB = snB;
    }
    public int getYellownormal() {
        return yellowNormal;
    }

    public void setYellownormal(int yellowNormal) {
        this.yellowNormal = yellowNormal;
    }
    public None getRedn() {
        return redN;
    }

    public void setRedn(None redN) {
        this.redN = redN;
    }
    public int getWon() {
        return won;
    }

    public void setWon(int won) {
        this.won = won;
    }
    public String getPreboard1() {
        return preBoard1;
    }

    public void setPreboard1(String preBoard1) {
        this.preBoard1 = preBoard1;
    }
    public None getYellown() {
        return yellowN;
    }

    public void setYellown(None yellowN) {
        this.yellowN = yellowN;
    }
    public int getPretomove2() {
        return preToMove2;
    }

    public void setPretomove2(int preToMove2) {
        this.preToMove2 = preToMove2;
    }
    public None getHlp() {
        return hlp;
    }

    public void setHlp(None hlp) {
        this.hlp = hlp;
    }
    public None getBp() {
        return bp;
    }

    public void setBp(None bp) {
        this.bp = bp;
    }
    public None getPlayers() {
        return players;
    }

    public void setPlayers(None players) {
        this.players = players;
    }
    public None getRp() {
        return rp;
    }

    public void setRp(None rp) {
        this.rp = rp;
    }
    public None getCol() {
        return col;
    }

    public void setCol(None col) {
        this.col = col;
    }
    public None getMup() {
        return mup;
    }

    public void setMup(None mup) {
        this.mup = mup;
    }
    public String getPreboard3() {
        return preBoard3;
    }

    public void setPreboard3(String preBoard3) {
        this.preBoard3 = preBoard3;
    }
    public None getMsg() {
        return msg;
    }

    public void setMsg(None msg) {
        this.msg = msg;
    }
    public None getColors() {
        return colors;
    }

    public void setColors(None colors) {
        this.colors = colors;
    }
    public None getBpt() {
        return bpt;
    }

    public void setBpt(None bpt) {
        this.bpt = bpt;
    }
    public int getPretomove3() {
        return preToMove3;
    }

    public void setPretomove3(int preToMove3) {
        this.preToMove3 = preToMove3;
    }
    public None getMode() {
        return mode;
    }

    public void setMode(None mode) {
        this.mode = mode;
    }
    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }
    public None getRkt() {
        return rkt;
    }

    public void setRkt(None rkt) {
        this.rkt = rkt;
    }
    public None getLevel() {
        return level;
    }

    public void setLevel(None level) {
        this.level = level;
    }
    public String getSelectedcolor() {
        return selectedColor;
    }

    public void setSelectedcolor(String selectedColor) {
        this.selectedColor = selectedColor;
    }
    public int getUndocount() {
        return undoCount;
    }

    public void setUndocount(int undoCount) {
        this.undoCount = undoCount;
    }
    public int getRedking() {
        return redKing;
    }

    public void setRedking(int redKing) {
        this.redKing = redKing;
    }
    public None getHlpb() {
        return hlpB;
    }

    public void setHlpb(None hlpB) {
        this.hlpB = hlpB;
    }
    public None getNwb() {
        return nwB;
    }

    public void setNwb(None nwB) {
        this.nwB = nwB;
    }
    public boolean getMovable() {
        return movable;
    }

    public void setMovable(boolean movable) {
        this.movable = movable;
    }
    public None getG() {
        return g;
    }

    public void setG(None g) {
        this.g = g;
    }
    public boolean getSilent() {
        return silent;
    }

    public void setSilent(boolean silent) {
        this.silent = silent;
    }
    public None getRk() {
        return rk;
    }

    public void setRk(None rk) {
        this.rk = rk;
    }
    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }
    public None getBk() {
        return bk;
    }

    public void setBk(None bk) {
        this.bk = bk;
    }
    public boolean getIncomplete() {
        return incomplete;
    }

    public void setIncomplete(boolean incomplete) {
        this.incomplete = incomplete;
    }
    public int getCurrtype() {
        return currType;
    }

    public void setCurrtype(int currType) {
        this.currType = currType;
    }
    public None getWinpoint() {
        return winPoint;
    }

    public void setWinpoint(None winPoint) {
        this.winPoint = winPoint;
    }
    public int getLoser() {
        return loser;
    }

    public void setLoser(int loser) {
        this.loser = loser;
    }
    public None getRpt() {
        return rpt;
    }

    public void setRpt(None rpt) {
        this.rpt = rpt;
    }
    public None getUnb() {
        return unB;
    }

    public void setUnb(None unB) {
        this.unB = unB;
    }
    public int getTomove() {
        return toMove;
    }

    public void setTomove(int toMove) {
        this.toMove = toMove;
    }
    public int getSelectedmode() {
        return selectedMode;
    }

    public void setSelectedmode(int selectedMode) {
        this.selectedMode = selectedMode;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getPreboard2() {
        return preBoard2;
    }

    public void setPreboard2(String preBoard2) {
        this.preBoard2 = preBoard2;
    }
    public None getC1() {
        return c1;
    }

    public void setC1(None c1) {
        this.c1 = c1;
    }
    public None getRedk() {
        return redK;
    }

    public void setRedk(None redK) {
        this.redK = redK;
    }
    public None getBkt() {
        return bkt;
    }

    public void setBkt(None bkt) {
        this.bkt = bkt;
    }
    public int getRednormal() {
        return redNormal;
    }

    public void setRednormal(int redNormal) {
        this.redNormal = redNormal;
    }


}