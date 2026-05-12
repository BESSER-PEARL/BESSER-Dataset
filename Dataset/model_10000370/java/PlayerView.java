





import java.util.List;
import java.util.ArrayList;

public class PlayerView  {

    private None busted;
    private None cardTotal;
    private None cardLabels;
    private None status;
    private None moneyBox;
    private None player;





    private GameView gameview;




    private BasePlayer baseplayer;


    public PlayerView(
        None busted,        None cardTotal,        None cardLabels,        None status,        None moneyBox,        None player    ) {
        this.busted = busted;
        this.cardTotal = cardTotal;
        this.cardLabels = cardLabels;
        this.status = status;
        this.moneyBox = moneyBox;
        this.player = player;
    }


    public None getBusted() {
        return busted;
    }

    public void setBusted(None busted) {
        this.busted = busted;
    }
    public None getCardtotal() {
        return cardTotal;
    }

    public void setCardtotal(None cardTotal) {
        this.cardTotal = cardTotal;
    }
    public None getCardlabels() {
        return cardLabels;
    }

    public void setCardlabels(None cardLabels) {
        this.cardLabels = cardLabels;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public None getMoneybox() {
        return moneyBox;
    }

    public void setMoneybox(None moneyBox) {
        this.moneyBox = moneyBox;
    }
    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }

    public GameView getGameview() {
        return gameview;
    }

    public void setGameview(GameView gameview) {
        this.gameview = gameview;
    }
    public BasePlayer getBaseplayer() {
        return baseplayer;
    }

    public void setBaseplayer(BasePlayer baseplayer) {
        this.baseplayer = baseplayer;
    }

}