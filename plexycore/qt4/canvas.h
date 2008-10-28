#ifndef _CANVAS_H_
#define _CANVAS_H_

#include <QtGui>

/**
 * \class Canvas
 * \brief 
 */
namespace PlexyDesk
{
  
class Canvas : public QGraphicsScene
{
  Q_OBJECT
public:
  Canvas ( QObject * parent = 0 );
  ~Canvas();
protected:
  void drawBackground ( QPainter * painter, const QRectF & rect );
private:
};
  
} /* PlexyDesk */


#endif /* _CANVAS_H_ */