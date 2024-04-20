import React from "react";
import { Steps as AntSteps } from "antd";
import PropTypes from "prop-types";

import { i18n } from "base/i18n";
import "antd/es/steps/style/css";

import styles from "./steps.css";

import CircleCheckIcon from "./circle-check.svg";

const { Step } = AntSteps;

export const STEPS_STATUS = {
  WAIT: "wait",
  PROCESS: "process",
  FINISH: "finish",
  ERROR: "error"
};

export const STEPS_DIRECTION = {
  VERTICAL: "vertical",
  HORIZONTAL: "horizontal"
};

export const STEPS_SIZE = {
  DEFAULT: "default",
  SMALL: "small",
  MEDIUM: "medium"
};

export const Steps = ({
  current,
  onChange,
  steps = [],
  direction = STEPS_DIRECTION.HORIZONTAL,
  size = STEPS_SIZE.SMALL,
  className = "",
  status = STEPS_STATUS.PROCESS
}) => {
  return (
    <AntSteps
      size={size}
      direction={direction}
      current={current}
      onChange={onChange}
      status={status}
      className={`${styles.customStep} ${className}`}
    >
      {steps.map((item, index) => (
        <Step
          key={index}
          description={item.description ? item.description : ""}
          title={item.titleRenderer || i18n._(item.title)}
          disabled={!!item.disabled}
          icon={current > index ? <CircleCheckIcon /> : item.icon}
        />
      ))}
    </AntSteps>
  );
};

Steps.propTypes = {
  /** The current step the user is in. */
  current: PropTypes.number,
  /** A callback function that get invoked when the step changes. */
  onChange: PropTypes.func.isRequired,
  /** An array of objects is used to represent each step, where each object follows the format {title: 'Step title'}." */
  steps: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.oneOfType([
        PropTypes.string.isRequired,
        PropTypes.node.isRequired
      ]),
      description: PropTypes.oneOfType([
        PropTypes.string.isRequired,
        PropTypes.node.isRequired
      ]),
      disabled: PropTypes.bool
    })
  ).isRequired,
  /** Direction props is used to display steps as horizontally and vertically */
  direction: PropTypes.oneOf(Object.values(STEPS_DIRECTION)).isRequired,
  /** specify the size of the step bar */
  size: PropTypes.oneOf(Object.values(STEPS_SIZE)).isRequired,
  /** specify the status of current step */
  status: PropTypes.oneOf(Object.values(STEPS_STATUS)),
  className: PropTypes.string
};

Steps.defaultProps = {
  steps: [],
  direction: STEPS_DIRECTION.HORIZONTAL
};

export { AntSteps };


story books views

import React from "react";

import { Steps, STEPS_DIRECTION, STEPS_STATUS } from "../index";

function StepsPlayground(args) {
  return <Steps {...args} />;
}

/** The Stepper component simplifies user progress tracking by displaying a sequence of steps in a visually appealing and interactive manner.  */
export default {
  component: Steps,
  title: "Navigation/Steps",
  tags: ["autodocs"],
  argTypes: {
    direction: {
      options: [STEPS_DIRECTION.VERTICAL, STEPS_DIRECTION.HORIZONTAL],
      control: {
        type: "select",
        labels: {
          [STEPS_DIRECTION.VERTICAL]: "STEPS_DIRECTION.VERTICAL",
          [STEPS_DIRECTION.HORIZONTAL]: "STEPS_DIRECTION.HORIZONTAL"
        }
      }
    },
    status: {
      options: [
        STEPS_STATUS.PROCESS,
        STEPS_STATUS.WAIT,
        STEPS_STATUS.ERROR,
        STEPS_STATUS.FINISH
      ],
      control: {
        type: "radio"
      }
    }
  },
  args: {
    direction: STEPS_DIRECTION.HORIZONTAL,
    current: 0,
    status: STEPS_STATUS.PROCESS,
    steps: [
      {
        title: "Domains"
      },
      {
        title: "User/Groups"
      },
      {
        title: "Attribute mapping"
      },
      {
        title: "Preferences"
      }
    ]
  }
};

/** In default mode, the stepper is rendered in horizontal direction.  */
export const Normal = {
  render: StepsPlayground
};

/** Vertical stepper  */
export const Vertical = {
  render: StepsPlayground,
  args: {
    direction: "vertical"
  }
};
