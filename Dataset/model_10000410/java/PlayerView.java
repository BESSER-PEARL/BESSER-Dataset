





import java.util.List;
import java.util.ArrayList;

public class PlayerView  {

    private None player;
    private None status;
    private None busted;
    private None moneyBox;
    private None cardTotal;
    private None cardLabels;





    private GameView gameview;




    private BasePlayer baseplayer;


    public PlayerView(
        None player,        None status,        None busted,        None moneyBox,        None cardTotal,        None cardLabels    ) {
        this.player = player;
        this.status = status;
        this.busted = busted;
        this.moneyBox = moneyBox;
        this.cardTotal = cardTotal;
        this.cardLabels = cardLabels;
    }


    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public None getBusted() {
        return busted;
    }

    public void setBusted(None busted) {
        this.busted = busted;
    }
    public None getMoneybox() {
        return moneyBox;
    }

    public void setMoneybox(None moneyBox) {
        this.moneyBox = moneyBox;
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